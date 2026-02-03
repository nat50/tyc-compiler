"""
Lexer test cases for TyC compiler
TODO: Implement 100 test cases for lexer
"""

import pytest
from tests.utils import Tokenizer


# ========== Simple Test Cases (10 types) ==========
def test_keyword_auto():
    """1. Keyword"""
    tokenizer = Tokenizer("auto")
    assert tokenizer.get_tokens_as_string() == "auto,<EOF>"


def test_operator_assign():
    """2. Operator"""
    tokenizer = Tokenizer("=")
    assert tokenizer.get_tokens_as_string() == "=,<EOF>"


def test_separator_semi():
    """3. Separator"""
    tokenizer = Tokenizer(";")
    assert tokenizer.get_tokens_as_string() == ";,<EOF>"


def test_integer_single_digit():
    """4. Integer literal"""
    tokenizer = Tokenizer("5")
    assert tokenizer.get_tokens_as_string() == "5,<EOF>"


def test_float_decimal():
    """5. Float literal"""
    tokenizer = Tokenizer("3.14")
    assert tokenizer.get_tokens_as_string() == "3.14,<EOF>"


def test_string_simple():
    """6. String literal"""
    tokenizer = Tokenizer('"hello"')
    assert tokenizer.get_tokens_as_string() == "hello,<EOF>"


def test_identifier_simple():
    """7. Identifier"""
    tokenizer = Tokenizer("x")
    assert tokenizer.get_tokens_as_string() == "x,<EOF>"


def test_line_comment():
    """8. Line comment"""
    tokenizer = Tokenizer("// This is a comment")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


def test_integer_in_expression():
    """9. Mixed: integers and operator"""
    tokenizer = Tokenizer("5+10")
    assert tokenizer.get_tokens_as_string() == "5,+,10,<EOF>"


def test_complex_expression():
    """10. Complex: variable declaration"""
    tokenizer = Tokenizer("auto x = 5 + 3 * 2;")
    assert tokenizer.get_tokens_as_string() == "auto,x,=,5,+,3,*,2,;,<EOF>"

# comments and spaces
def test_whitespace_skipped():
    """11. Whitespace characters are skipped"""
    tokenizer = Tokenizer("   \t\r\n\f   ")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


def test_block_comment_skipped():
    """12. Block comment is skipped"""
    tokenizer = Tokenizer("/* This is a block comment */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


def test_line_comment_skipped():
    """13. Block comment spanning multiple lines"""
    tokenizer = Tokenizer("/* This is\na multiline\nblock comment */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


def test_block_comment_with_line_comment():
    """14. Block comment with // inside has no meaning"""
    tokenizer = Tokenizer("/* Block comment so // has no meaning here */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


def test_line_comment_with_block_comment():
    """15. Line comment with /* inside has no meaning"""
    tokenizer = Tokenizer("// Line comment so /* has no meaning here")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


# keywords
def test_type_keywords():
    """16. Type keywords"""
    tokenizer = Tokenizer("int float string void")
    assert tokenizer.get_tokens_as_string() == "int,float,string,void,<EOF>"


def test_control_flow_keywords():
    """17. Control flow keywords"""
    tokenizer = Tokenizer("if else while for switch case default")
    assert tokenizer.get_tokens_as_string() == "if,else,while,for,switch,case,default,<EOF>"


def test_jump_keywords():
    """18. Jump keywords"""
    tokenizer = Tokenizer("break continue return")
    assert tokenizer.get_tokens_as_string() == "break,continue,return,<EOF>"


def test_auto_struct_keywords():
    """19. Auto and struct keywords"""
    tokenizer = Tokenizer("auto struct")
    assert tokenizer.get_tokens_as_string() == "auto,struct,<EOF>"


def test_keyword_like_identifiers():
    """20. Keyword-like identifiers are separate"""
    tokenizer = Tokenizer("auto auto1 integer floatValue")
    assert tokenizer.get_tokens_as_string() == "auto,auto1,integer,floatValue,<EOF>"


# identifiers
def test_simple_identifiers():
    """21. Simple identifiers"""
    tokenizer = Tokenizer("Tan HCMUT student")
    assert tokenizer.get_tokens_as_string() == "Tan,HCMUT,student,<EOF>"


def test_underscore_identifiers():
    """22. Underscore identifiers"""
    tokenizer = Tokenizer("_ _private __init__")
    assert tokenizer.get_tokens_as_string() == "_,_private,__init__,<EOF>"


def test_identifiers_with_numbers():
    """23. Identifiers with numbers"""
    tokenizer = Tokenizer("var1 student2024 x123y")
    assert tokenizer.get_tokens_as_string() == "var1,student2024,x123y,<EOF>"


def test_case_sensitivity():
    """24. Case sensitivity"""
    tokenizer = Tokenizer("MyVar myvar MYVAR myVAR")
    assert tokenizer.get_tokens_as_string() == "MyVar,myvar,MYVAR,myVAR,<EOF>"


def test_long_identifier():
    """25. Long identifier"""
    tokenizer = Tokenizer("HoChiMinhCityUniversityOfTechnology_CSE_k23_Tandeptrai")
    assert tokenizer.get_tokens_as_string() == "HoChiMinhCityUniversityOfTechnology_CSE_k23_Tandeptrai,<EOF>"


# integer literals
def test_single_digit_integers():
    """26. Single digit integers"""
    tokenizer = Tokenizer("0 1 5 9")
    assert tokenizer.get_tokens_as_string() == "0,1,5,9,<EOF>"


def test_multi_digit_integers():
    """27. Multi-digit integers"""
    tokenizer = Tokenizer("100 255 2024 123456789")
    assert tokenizer.get_tokens_as_string() == "100,255,2024,123456789,<EOF>"


def test_negative_integer():
    """28. Negative integer (MINUS + INTLIT)"""
    tokenizer = Tokenizer("-45 -100")
    assert tokenizer.get_tokens_as_string() == "-,45,-,100,<EOF>"


def test_integer_followed_by_identifier():
    """29. Integer followed by identifier"""
    tokenizer = Tokenizer("123abc 456def")
    assert tokenizer.get_tokens_as_string() == "123,abc,456,def,<EOF>"


def test_zeros():
    """30. Zeros"""
    tokenizer = Tokenizer("0 00")
    assert tokenizer.get_tokens_as_string() == "0,0,0,<EOF>"


# float literals
def test_simple_floats():
    """31. Simple floats"""
    tokenizer = Tokenizer("0.0 3.14 123.456")
    assert tokenizer.get_tokens_as_string() == "0.0,3.14,123.456,<EOF>"


def test_float_trailing_leading_dot():
    """32. Float with trailing/leading dot"""
    tokenizer = Tokenizer("1. .5 0.")
    assert tokenizer.get_tokens_as_string() == "1.,.5,0.,<EOF>"


def test_scientific_notation_lowercase():
    """33. Scientific notation lowercase e"""
    tokenizer = Tokenizer("1e10 1.5e4 .5e3")
    assert tokenizer.get_tokens_as_string() == "1e10,1.5e4,.5e3,<EOF>"


def test_scientific_notation_uppercase():
    """34. Scientific notation uppercase E"""
    tokenizer = Tokenizer("1E10 2.5E4 .7E2")
    assert tokenizer.get_tokens_as_string() == "1E10,2.5E4,.7E2,<EOF>"


def test_scientific_notation_negative_exponent():
    """35. Scientific notation with negative exponent"""
    tokenizer = Tokenizer("5.67e-2 1.23E-10")
    assert tokenizer.get_tokens_as_string() == "5.67e-2,1.23E-10,<EOF>"


# string literals
def test_string_with_tab():
    """36. String containing tab"""
    tokenizer = Tokenizer('"This is a string containing tab \\t"')
    assert tokenizer.get_tokens_as_string() == 'This is a string containing tab \\t,<EOF>'


def test_empty_string():
    """37. Empty string"""
    tokenizer = Tokenizer('""')
    assert tokenizer.get_tokens_as_string() == ",<EOF>"


def test_string_with_escaped_quotes():
    """38. String with escaped quotes"""
    tokenizer = Tokenizer(r'"He asked me: \"Where is John?\""')
    assert tokenizer.get_tokens_as_string() == r'He asked me: \"Where is John?\",<EOF>'


def test_string_with_unprintable():
    """39. String with unprintable character"""
    tokenizer = Tokenizer('"String with unprintable: \x01"')
    assert tokenizer.get_tokens_as_string() == 'String with unprintable: \x01,<EOF>'


def test_string_extended_ascii():
    """40. String with extended ASCII"""
    tokenizer = Tokenizer('"Extended ASCII: \x80\xFF"')
    assert tokenizer.get_tokens_as_string() == 'Extended ASCII: \x80\xFF,<EOF>'

# operators
def test_arithmetic_operators():
    """41. Arithmetic operators"""
    tokenizer = Tokenizer("+ - * / %")
    assert tokenizer.get_tokens_as_string() == "+,-,*,/,%,<EOF>"


def test_comparison_operators():
    """42. Comparison operators"""
    tokenizer = Tokenizer("== != < > <= >=")
    assert tokenizer.get_tokens_as_string() == "==,!=,<,>,<=,>=,<EOF>"


def test_logical_operators():
    """43. Logical operators"""
    tokenizer = Tokenizer("&& || !")
    assert tokenizer.get_tokens_as_string() == "&&,||,!,<EOF>"


def test_inc_dec_assign_dot():
    """44. Increment, decrement, assignment, dot"""
    tokenizer = Tokenizer("++ -- = .")
    assert tokenizer.get_tokens_as_string() == "++,--,=,.,<EOF>"


def test_operator_disambiguation():
    """45. Operator disambiguation"""
    tokenizer = Tokenizer("+ ++ = == < <= > >= ! != - --")
    assert tokenizer.get_tokens_as_string() == "+,++,=,==,<,<=,>,>=,!,!=,-,--,<EOF>"


# separators
def test_parentheses_braces():
    """46. Parentheses and braces"""
    tokenizer = Tokenizer("( ) { }")
    assert tokenizer.get_tokens_as_string() == "(,),{,},<EOF>"


def test_brackets():
    """47. Error token ["""
    tokenizer = Tokenizer("[")
    assert tokenizer.get_tokens_as_string() == "Error Token ["


def test_semicolon_comma():
    """48. Semicolon and comma"""
    tokenizer = Tokenizer("; , ; ,")
    assert tokenizer.get_tokens_as_string() == ";,,,;,,,<EOF>"


def test_colon():
    """49. Colon"""
    tokenizer = Tokenizer(": : :")
    assert tokenizer.get_tokens_as_string() == ":,:,:,<EOF>"


def test_all_separators():
    """50. All separators together"""
    tokenizer = Tokenizer("(){}:;,")
    assert tokenizer.get_tokens_as_string() == "(,),{,},:,;,,,<EOF>"

# error tokens - invalid characters
def test_error_at_symbol():
    """51. Error token @"""
    tokenizer = Tokenizer("@")
    assert tokenizer.get_tokens_as_string() == "Error Token @"


def test_error_hash_symbol():
    """52. Error token #"""
    tokenizer = Tokenizer("#")
    assert tokenizer.get_tokens_as_string() == "Error Token #"


def test_error_dollar_symbol():
    """53. Error token $"""
    tokenizer = Tokenizer("$")
    assert tokenizer.get_tokens_as_string() == "Error Token $"


def test_error_backtick():
    """54. Error token backtick"""
    tokenizer = Tokenizer("`")
    assert tokenizer.get_tokens_as_string() == "Error Token `"


def test_error_tilde():
    """55. Error token tilde"""
    tokenizer = Tokenizer("~")
    assert tokenizer.get_tokens_as_string() == "Error Token ~"


# error tokens - string errors
def test_unclosed_string_simple():
    """56. Unclosed string - simple"""
    tokenizer = Tokenizer('"unclosed')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: unclosed"


def test_unclosed_string_newline():
    """57. Unclosed string with newline"""
    tokenizer = Tokenizer('"Tan HCMUT\n')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: Tan HCMUT\n"


def test_illegal_escape_z():
    """58. Illegal escape \\z"""
    tokenizer = Tokenizer('"bad\\z"')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: bad\\z"

def test_illegal_escape_a():
    """59. Illegal escape \\a"""
    tokenizer = Tokenizer(r'"Hello \a World"')
    assert tokenizer.get_tokens_as_string() == r"Illegal Escape In String: Hello \a"


def test_unclosed_string_escaped_newline():
    """60. Unclosed string with escaped newline"""
    tokenizer = Tokenizer('"abc\\\n')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: abc\\\n"


# complex tests
def test_full_var_decl_auto():
    """61. Full variable declaration with auto"""
    tokenizer = Tokenizer("auto Tan = 2005;")
    assert tokenizer.get_tokens_as_string() == "auto,Tan,=,2005,;,<EOF>"


def test_full_var_decl_int():
    """62. Full variable declaration with int type"""
    tokenizer = Tokenizer("int HCMUT_year = 1957;")
    assert tokenizer.get_tokens_as_string() == "int,HCMUT_year,=,1957,;,<EOF>"


def test_float_var_scientific():
    """63. Float variable with scientific notation"""
    tokenizer = Tokenizer("float pi = 3.14159e0;")
    assert tokenizer.get_tokens_as_string() == "float,pi,=,3.14159e0,;,<EOF>"


def test_string_var_escape_sequences():
    """64. String variable with escape sequences"""
    tokenizer = Tokenizer('string msg = "Hello\\tTan\\nWelcome to HCMUT!";')
    assert tokenizer.get_tokens_as_string() == 'string,msg,=,Hello\\tTan\\nWelcome to HCMUT!,;,<EOF>'


def test_struct_declaration():
    """65. Struct declaration"""
    tokenizer = Tokenizer("struct Student { string name; int age; float gpa; };")
    assert tokenizer.get_tokens_as_string() == "struct,Student,{,string,name,;,int,age,;,float,gpa,;,},;,<EOF>"


def test_function_void_main():
    """66. Function declaration void main"""
    tokenizer = Tokenizer("void main() { return; }")
    assert tokenizer.get_tokens_as_string() == "void,main,(,),{,return,;,},<EOF>"


def test_function_with_parameters():
    """67. Function with parameters"""
    tokenizer = Tokenizer("int add(int x, int y) { return x + y; }")
    assert tokenizer.get_tokens_as_string() == "int,add,(,int,x,,,int,y,),{,return,x,+,y,;,},<EOF>"


def test_if_else_statement():
    """68. If-else statement"""
    tokenizer = Tokenizer("if (x > 0) { y = 1; } else { y = 0; }")
    assert tokenizer.get_tokens_as_string() == "if,(,x,>,0,),{,y,=,1,;,},else,{,y,=,0,;,},<EOF>"


def test_while_loop_increment():
    """69. While loop with increment"""
    tokenizer = Tokenizer("while (i < 10) { ++i; }")
    assert tokenizer.get_tokens_as_string() == "while,(,i,<,10,),{,++,i,;,},<EOF>"


def test_for_loop_complete():
    """70. For loop complete"""
    tokenizer = Tokenizer("for (auto i = 0; i < n; ++i) { sum = sum + i; }")
    assert tokenizer.get_tokens_as_string() == "for,(,auto,i,=,0,;,i,<,n,;,++,i,),{,sum,=,sum,+,i,;,},<EOF>"


def test_switch_case_statement():
    """71. Switch-case statement"""
    tokenizer = Tokenizer("switch (day) { case 1: break; case 2: break; default: return; }")
    assert tokenizer.get_tokens_as_string() == "switch,(,day,),{,case,1,:,break,;,case,2,:,break,;,default,:,return,;,},<EOF>"


def test_nested_arithmetic_expression():
    """72. Nested arithmetic expression"""
    tokenizer = Tokenizer("result = (a + b) * (c - d) / e % f;")
    assert tokenizer.get_tokens_as_string() == "result,=,(,a,+,b,),*,(,c,-,d,),/,e,%,f,;,<EOF>"


def test_logical_expression_comparisons():
    """73. Logical expression with comparisons"""
    tokenizer = Tokenizer("if (x >= 0 && x <= 100 || y != 0) { flag = 1; }")
    assert tokenizer.get_tokens_as_string() == "if,(,x,>=,0,&&,x,<=,100,||,y,!=,0,),{,flag,=,1,;,},<EOF>"


def test_unary_operators():
    """74. Unary operators"""
    tokenizer = Tokenizer("x = -y + +z; flag = !condition;")
    assert tokenizer.get_tokens_as_string() == "x,=,-,y,+,+,z,;,flag,=,!,condition,;,<EOF>"


def test_increment_decrement_operators():
    """75. Increment and decrement operators"""
    tokenizer = Tokenizer("++x; --y; a++; b--;")
    assert tokenizer.get_tokens_as_string() == "++,x,;,--,y,;,a,++,;,b,--,;,<EOF>"


def test_member_access_chain():
    """76. Member access chain"""
    tokenizer = Tokenizer("student.name = \"Tan\"; point.x = point.y + 10;")
    assert tokenizer.get_tokens_as_string() == "student,.,name,=,Tan,;,point,.,x,=,point,.,y,+,10,;,<EOF>"


def test_function_call_multiple_args():
    """77. Function call with multiple arguments"""
    tokenizer = Tokenizer("result = calculate(a, b, c, 100, 3.14);")
    assert tokenizer.get_tokens_as_string() == "result,=,calculate,(,a,,,b,,,c,,,100,,,3.14,),;,<EOF>"


def test_nested_function_calls():
    """78. Nested function calls"""
    tokenizer = Tokenizer("printInt(add(multiply(2, 3), 4));")
    assert tokenizer.get_tokens_as_string() == "printInt,(,add,(,multiply,(,2,,,3,),,,4,),),;,<EOF>"


def test_struct_initialization():
    """79. Struct initialization"""
    tokenizer = Tokenizer("Point p = {10, 20}; Person student = {\"Tan\", 22, 3.8};")
    assert tokenizer.get_tokens_as_string() == "Point,p,=,{,10,,,20,},;,Person,student,=,{,Tan,,,22,,,3.8,},;,<EOF>"


def test_if_else_if_chain():
    """80. Complete if-else-if chain"""
    tokenizer = Tokenizer("if (grade >= 90) { result = \"A\"; } else { if (grade >= 80) { result = \"B\"; } }")
    assert tokenizer.get_tokens_as_string() == "if,(,grade,>=,90,),{,result,=,A,;,},else,{,if,(,grade,>=,80,),{,result,=,B,;,},},<EOF>"


def test_nested_while_loops():
    """81. Nested while loops"""
    tokenizer = Tokenizer("while (i < 10) { while (j < 10) { matrix = i * j; ++j; } ++i; }")
    assert tokenizer.get_tokens_as_string() == "while,(,i,<,10,),{,while,(,j,<,10,),{,matrix,=,i,*,j,;,++,j,;,},++,i,;,},<EOF>"


def test_for_loop_break_continue():
    """82. For loop with break and continue"""
    tokenizer = Tokenizer("for (auto i = 0; i < 100; ++i) { if (i == 50) { break; } if (i % 2 == 0) { continue; } }")
    assert tokenizer.get_tokens_as_string() == "for,(,auto,i,=,0,;,i,<,100,;,++,i,),{,if,(,i,==,50,),{,break,;,},if,(,i,%,2,==,0,),{,continue,;,},},<EOF>"


def test_multiple_var_declarations():
    """83. Multiple variable declarations"""
    tokenizer = Tokenizer("int a; float b; string c; auto d = 10; Point p;")
    assert tokenizer.get_tokens_as_string() == "int,a,;,float,b,;,string,c,;,auto,d,=,10,;,Point,p,;,<EOF>"


def test_all_comparison_operators():
    """84. Expression with all comparison operators"""
    tokenizer = Tokenizer("result = (a == b) && (c != d) && (e < f) && (g > h) && (i <= j) && (k >= l);")
    assert tokenizer.get_tokens_as_string() == "result,=,(,a,==,b,),&&,(,c,!=,d,),&&,(,e,<,f,),&&,(,g,>,h,),&&,(,i,<=,j,),&&,(,k,>=,l,),;,<EOF>"


def test_code_with_comments():
    """85. Code with comments interspersed"""
    tokenizer = Tokenizer("int x = 10; /* comment */ int y = 20; // line comment\nint z = 30;")
    assert tokenizer.get_tokens_as_string() == "int,x,=,10,;,int,y,=,20,;,int,z,=,30,;,<EOF>"


def test_multiple_float_formats():
    """86. Multiple float formats in expression"""
    tokenizer = Tokenizer("result = 1.0 + .5 + 1. + 1e10 + 1.5e-3 + .5E2;")
    assert tokenizer.get_tokens_as_string() == "result,=,1.0,+,.5,+,1.,+,1e10,+,1.5e-3,+,.5E2,;,<EOF>"


def test_string_all_escape_sequences():
    """87. String with all valid escape sequences"""
    tokenizer = Tokenizer('"\\b\\f\\r\\n\\t\\"\\\\complete"')
    assert tokenizer.get_tokens_as_string() == '\\b\\f\\r\\n\\t\\"\\\\complete,<EOF>'


def test_factorial_function():
    """88. Factorial function - Tan HCMUT"""
    tokenizer = Tokenizer("int factorial(int n) { if (n <= 1) { return 1; } return n * factorial(n - 1); }")
    assert tokenizer.get_tokens_as_string() == "int,factorial,(,int,n,),{,if,(,n,<=,1,),{,return,1,;,},return,n,*,factorial,(,n,-,1,),;,},<EOF>"


def test_deeply_nested_parentheses():
    """89. Deeply nested parentheses"""
    tokenizer = Tokenizer("x = ((((a + b) * c) - d) / e);")
    assert tokenizer.get_tokens_as_string() == "x,=,(,(,(,(,a,+,b,),*,c,),-,d,),/,e,),;,<EOF>"


def test_mixed_integers_floats():
    """90. Mixed integers and floats in expression"""
    tokenizer = Tokenizer("result = 10 + 3.14 - 5 * 2.5 / 2 % 3;")
    assert tokenizer.get_tokens_as_string() == "result,=,10,+,3.14,-,5,*,2.5,/,2,%,3,;,<EOF>"


def test_assignment_chain():
    """91. Assignment chain"""
    tokenizer = Tokenizer("a = b = c = d = 0;")
    assert tokenizer.get_tokens_as_string() == "a,=,b,=,c,=,d,=,0,;,<EOF>"


def test_chained_member_access():
    """92. Chained member access with assignment"""
    tokenizer = Tokenizer("university.department.student.name = \"Tan\"; university.department.student.gpa = 3.8;")
    assert tokenizer.get_tokens_as_string() == "university,.,department,.,student,.,name,=,Tan,;,university,.,department,.,student,.,gpa,=,3.8,;,<EOF>"


def test_ternary_like_if():
    """93. Scientific notation with explicit positive exponent"""
    tokenizer = Tokenizer("1e+10 2.5E+4 .3e+2")
    assert tokenizer.get_tokens_as_string() == "1e+10,2.5E+4,.3e+2,<EOF>"


def test_switch_fall_through():
    """94. Complex switch with fall-through"""
    tokenizer = Tokenizer("switch (grade) { case 10: case 9: result = \"A\"; break; case 8: case 7: result = \"B\"; break; default: result = \"C\"; }")
    assert tokenizer.get_tokens_as_string() == "switch,(,grade,),{,case,10,:,case,9,:,result,=,A,;,break,;,case,8,:,case,7,:,result,=,B,;,break,;,default,:,result,=,C,;,},<EOF>"


def test_complex_boolean_expression():
    """95. Complex boolean expression"""
    tokenizer = Tokenizer("valid = (age >= 18 && age <= 65) || (hasPermission && !isRestricted);")
    assert tokenizer.get_tokens_as_string() == "valid,=,(,age,>=,18,&&,age,<=,65,),||,(,hasPermission,&&,!,isRestricted,),;,<EOF>"


def test_io_functions():
    """96. IO functions"""
    tokenizer = Tokenizer("int x = readInt(); float y = readFloat(); string s = readString(); printInt(x); printFloat(y); printString(s);")
    assert tokenizer.get_tokens_as_string() == "int,x,=,readInt,(,),;,float,y,=,readFloat,(,),;,string,s,=,readString,(,),;,printInt,(,x,),;,printFloat,(,y,),;,printString,(,s,),;,<EOF>"


def test_struct_with_member_access():
    """97. Complete struct with member access"""
    tokenizer = Tokenizer("struct HCMUT { string name; int established; }; HCMUT uni = {\"Ho Chi Minh City University of Technology\", 1957}; printString(uni.name);")
    assert tokenizer.get_tokens_as_string() == "struct,HCMUT,{,string,name,;,int,established,;,},;,HCMUT,uni,=,{,Ho Chi Minh City University of Technology,,,1957,},;,printString,(,uni,.,name,),;,<EOF>"


def test_multiple_statements_same_line():
    """98. Multiple statements on same line"""
    tokenizer = Tokenizer("a=1;b=2;c=3;d=a+b+c;")
    assert tokenizer.get_tokens_as_string() == "a,=,1,;,b,=,2,;,c,=,3,;,d,=,a,+,b,+,c,;,<EOF>"


def test_no_spaces_between_tokens():
    """99. No spaces between tokens"""
    tokenizer = Tokenizer("if(x>0){y=x*2;}else{y=-x;}")
    assert tokenizer.get_tokens_as_string() == "if,(,x,>,0,),{,y,=,x,*,2,;,},else,{,y,=,-,x,;,},<EOF>"


def test_postfix_prefix_expression():
    """100. Postfix and prefix in same expression"""
    tokenizer = Tokenizer("result = ++a + b++ - --c + d--;")
    assert tokenizer.get_tokens_as_string() == "result,=,++,a,+,b,++,-,--,c,+,d,--,;,<EOF>"