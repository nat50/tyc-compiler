"""
Parser test cases for TyC compiler
TODO: Implement 100 test cases for parser
"""

import pytest
from tests.utils import Parser


# ========== Simple Test Cases (10 types) ==========
def test_empty_program():
    """1. Empty program"""
    assert Parser("").parse() == "success"


def test_program_with_only_main():
    """2. Program with only main function"""
    assert Parser("void main() {}").parse() == "success"


def test_struct_simple():
    """3. Struct declaration"""
    source = "struct Point { int x; int y; };"
    assert Parser(source).parse() == "success"


def test_function_no_params():
    """4. Function with no parameters"""
    source = "void greet() { printString(\"Hello\"); }"
    assert Parser(source).parse() == "success"


def test_var_decl_auto_with_init():
    """5. Variable declaration"""
    source = "void main() { auto x = 5; }"
    assert Parser(source).parse() == "success"


def test_if_simple():
    """6. If statement"""
    source = "void main() { if (1) printInt(1); }"
    assert Parser(source).parse() == "success"


def test_while_simple():
    """7. While statement"""
    source = "void main() { while (1) printInt(1); }"
    assert Parser(source).parse() == "success"


def test_for_simple():
    """8. For statement"""
    source = "void main() { for (auto i = 0; i < 10; ++i) printInt(i); }"
    assert Parser(source).parse() == "success"


def test_switch_simple():
    """9. Switch statement"""
    source = "void main() { switch (1) { case 1: printInt(1); break; } }"
    assert Parser(source).parse() == "success"


def test_assignment_simple():
    """10. Assignment statement"""
    source = "void main() { int x; x = 5; }"
    assert Parser(source).parse() == "success"


# Struct Tests
def test_struct_empty():
    """11. Empty struct"""
    source = "struct Empty {};"
    assert Parser(source).parse() == "success"


def test_struct_single_member():
    """12. Struct with single member"""
    source = "struct Tan { int id; };"
    assert Parser(source).parse() == "success"


def test_struct_multiple_members():
    """13. Struct with multiple members"""
    source = "struct HCMUT { string name; int year; float rating; };"
    assert Parser(source).parse() == "success"


def test_struct_nested_type():
    """14. Struct with another struct as member type"""
    source = "struct Point { int x; int y; }; struct Line { Point start; Point end; };"
    assert Parser(source).parse() == "success"


def test_struct_multiple_declarations():
    """15. Multiple struct declarations"""
    source = "struct A { int x; }; struct B { float y; }; struct C { string z; };"
    assert Parser(source).parse() == "success"


def test_struct_with_function():
    """16. Struct declaration followed by function"""
    source = "struct Student { string name; int age; }; void main() {}"
    assert Parser(source).parse() == "success"


def test_struct_before_and_after_function():
    """17. Structs before and after function"""
    source = "struct A { int x; }; void main() {} struct B { int y; };"
    assert Parser(source).parse() == "success"


def test_struct_member_same_name():
    """18. Struct member with struct type name as identifier"""
    source = "struct Point { int Point; };"
    assert Parser(source).parse() == "success"


def test_struct_all_primitive_types():
    """19. Struct with all primitive types"""
    source = "struct AllTypes { int i; float f; string s; };"
    assert Parser(source).parse() == "success"


def test_struct_deeply_nested():
    """20. Deeply nested struct types"""
    source = "struct A { int x; }; struct B { A a; }; struct C { B b; }; struct D { C c; };"
    assert Parser(source).parse() == "success"


# Function Tests
def test_function_single_param():
    """21. Function with single parameter"""
    source = "void greet(string name) { printString(name); }"
    assert Parser(source).parse() == "success"


def test_function_multiple_params():
    """22. Function with multiple parameters"""
    source = "int add(int x, int y, int z) { return x + y + z; }"
    assert Parser(source).parse() == "success"


def test_function_return_int():
    """23. Function returning int"""
    source = "int getTan() { return 2005; }"
    assert Parser(source).parse() == "success"


def test_function_return_float():
    """24. Function returning float"""
    source = "float getPI() { return 3.14159; }"
    assert Parser(source).parse() == "success"


def test_function_return_string():
    """25. Function returning string"""
    source = "string getSchool() { return \"HCMUT\"; }"
    assert Parser(source).parse() == "success"


def test_function_struct_param():
    """26. Function with struct parameter"""
    source = "struct Point { int x; int y; }; void printPoint(Point p) { printInt(p.x); }"
    assert Parser(source).parse() == "success"


def test_function_struct_return():
    """27. Function returning struct type"""
    source = "struct Point { int x; int y; }; Point createPoint(int x, int y) { Point p = {x, y}; return p; }"
    assert Parser(source).parse() == "success"


def test_function_inferred_return():
    """28. Function with inferred return type"""
    source = "add(int x, int y) { return x + y; }"
    assert Parser(source).parse() == "success"


def test_function_multiple_functions():
    """29. Multiple function declarations"""
    source = "void f1() {} void f2() {} void f3() {} void main() {}"
    assert Parser(source).parse() == "success"


def test_function_recursive():
    """30. Recursive function"""
    source = "int factorial(int n) { if (n <= 1) { return 1; } return n * factorial(n - 1); }"
    assert Parser(source).parse() == "success"


# Variable Declaration Tests
def test_var_decl_int():
    """31. Variable declaration with int type"""
    source = "void main() { int Tan; }"
    assert Parser(source).parse() == "success"


def test_var_decl_float():
    """32. Variable declaration with float type"""
    source = "void main() { float gpa; }"
    assert Parser(source).parse() == "success"


def test_var_decl_string():
    """33. Variable declaration with string type"""
    source = "void main() { string school; }"
    assert Parser(source).parse() == "success"


def test_var_decl_int_init():
    """34. Variable declaration with int initialization"""
    source = "void main() { int year = 2026; }"
    assert Parser(source).parse() == "success"


def test_var_decl_float_init():
    """35. Variable declaration with float initialization"""
    source = "void main() { float pi = 3.14; }"
    assert Parser(source).parse() == "success"


def test_var_decl_string_init():
    """36. Variable declaration with string initialization"""
    source = "void main() { string name = \"Tan\"; }"
    assert Parser(source).parse() == "success"


def test_var_decl_auto_no_init():
    """37. Variable declaration with auto without init"""
    source = "void main() { auto x; }"
    assert Parser(source).parse() == "success"


def test_var_decl_struct_type():
    """38. Variable declaration with struct type"""
    source = "struct HCMUT { int year; }; void main() { HCMUT uni; }"
    assert Parser(source).parse() == "success"


def test_var_decl_struct_init():
    """39. Variable declaration with struct initialization"""
    source = "struct Point { int x; int y; }; void main() { Point p = {10, 20}; }"
    assert Parser(source).parse() == "success"


def test_var_decl_multiple():
    """40. Multiple variable declarations"""
    source = "void main() { int a; float b; string c; auto d = 1; }"
    assert Parser(source).parse() == "success"


# If Statement Tests
def test_if_with_block():
    """41. If statement with block"""
    source = "void main() { if (1) { printInt(1); } }"
    assert Parser(source).parse() == "success"


def test_if_else():
    """42. If-else statement"""
    source = "void main() { if (1) printInt(1); else printInt(0); }"
    assert Parser(source).parse() == "success"


def test_if_else_blocks():
    """43. If-else with blocks"""
    source = "void main() { if (x > 0) { printInt(1); } else { printInt(0); } }"
    assert Parser(source).parse() == "success"


def test_if_nested():
    """44. Nested if statements"""
    source = "void main() { if (a) if (b) printInt(1); else printInt(2); }"
    assert Parser(source).parse() == "success"


def test_if_complex_condition():
    """45. If with complex condition"""
    source = "void main() { if (x >= 0 && x <= 100 || y != 0) { printInt(x); } }"
    assert Parser(source).parse() == "success"


# While Statement Tests
def test_while_with_block():
    """46. While statement with block"""
    source = "void main() { while (i < 10) { ++i; } }"
    assert Parser(source).parse() == "success"


def test_while_nested():
    """47. Nested while loops"""
    source = "void main() { while (i < 10) { while (j < 10) { ++j; } ++i; } }"
    assert Parser(source).parse() == "success"


def test_while_with_break():
    """48. While with break"""
    source = "void main() { while (1) { break; } }"
    assert Parser(source).parse() == "success"


def test_while_with_continue():
    """49. While with continue"""
    source = "void main() { while (i < 10) { ++i; continue; } }"
    assert Parser(source).parse() == "success"


def test_while_complex_body():
    """50. While with complex body"""
    source = "void main() { while (i < 10) { if (i == 5) break; printInt(i); ++i; } }"
    assert Parser(source).parse() == "success"


# For Statement Tests
def test_for_all_parts():
    """51. For with all parts"""
    source = "void main() { for (auto i = 0; i < 10; ++i) { printInt(i); } }"
    assert Parser(source).parse() == "success"


def test_for_empty_init():
    """52. For with empty init"""
    source = "void main() { int i; for (; i < 10; ++i) printInt(i); }"
    assert Parser(source).parse() == "success"


def test_for_empty_condition():
    """53. For with empty condition (infinite loop)"""
    source = "void main() { for (auto i = 0; ; ++i) { if (i > 10) break; } }"
    assert Parser(source).parse() == "success"


def test_for_empty_update():
    """54. For with empty update"""
    source = "void main() { for (auto i = 0; i < 10;) { ++i; } }"
    assert Parser(source).parse() == "success"


def test_for_all_empty():
    """55. For with all parts empty"""
    source = "void main() { for (;;) { break; } }"
    assert Parser(source).parse() == "success"


# Switch Statement Tests
def test_switch_multiple_cases():
    """56. Switch with multiple cases"""
    source = "void main() { switch (x) { case 1: printInt(1); break; case 2: printInt(2); break; } }"
    assert Parser(source).parse() == "success"


def test_switch_with_default():
    """57. Switch with default"""
    source = "void main() { switch (x) { case 1: printInt(1); break; default: printInt(0); } }"
    assert Parser(source).parse() == "success"


def test_switch_fall_through():
    """58. Switch with fall-through"""
    source = "void main() { switch (x) { case 1: case 2: printInt(12); break; default: printInt(0); } }"
    assert Parser(source).parse() == "success"


def test_switch_empty():
    """59. Switch with empty body"""
    source = "void main() { switch (x) {} }"
    assert Parser(source).parse() == "success"


def test_switch_nested():
    """60. Nested switch statements"""
    source = "void main() { switch (x) { case 1: switch (y) { case 2: break; } break; } }"
    assert Parser(source).parse() == "success"


# Expression Tests
def test_expr_arithmetic():
    """61. Arithmetic expression"""
    source = "void main() { auto x = 1 + 2 - 3 * 4 / 5 % 6; }"
    assert Parser(source).parse() == "success"


def test_expr_relational():
    """62. Relational expression"""
    source = "void main() { auto x = a < b && c > d && e <= f && g >= h; }"
    assert Parser(source).parse() == "success"


def test_expr_equality():
    """63. Equality expression"""
    source = "void main() { auto x = a == b && c != d; }"
    assert Parser(source).parse() == "success"


def test_expr_logical():
    """64. Logical expression"""
    source = "void main() { auto x = a && b || c && !d; }"
    assert Parser(source).parse() == "success"


def test_expr_unary():
    """65. Unary expression"""
    source = "void main() { auto x = -a + +b + !c; }"
    assert Parser(source).parse() == "success"


def test_expr_increment_prefix():
    """66. Prefix increment/decrement"""
    source = "void main() { ++x; --y; }"
    assert Parser(source).parse() == "success"


def test_expr_increment_postfix():
    """67. Postfix increment/decrement"""
    source = "void main() { x++; y--; }"
    assert Parser(source).parse() == "success"


def test_expr_member_access():
    """68. Member access expression"""
    source = "struct Point { int x; int y; }; void main() { Point p; auto x = p.x + p.y; }"
    assert Parser(source).parse() == "success"


def test_expr_chained_member():
    """69. Chained member access"""
    source = "struct A { int x; }; struct B { A a; }; void main() { B b; auto x = b.a.x; }"
    assert Parser(source).parse() == "success"


def test_expr_function_call():
    """70. Function call expression"""
    source = "int add(int x, int y) { return x + y; } void main() { auto r = add(1, 2); }"
    assert Parser(source).parse() == "success"


def test_expr_nested_function_call():
    """71. Nested function calls"""
    source = "int f(int x) { return x; } void main() { auto r = f(f(f(1))); }"
    assert Parser(source).parse() == "success"


def test_expr_parenthesized():
    """72. Parenthesized expression"""
    source = "void main() { auto x = (1 + 2) * (3 - 4); }"
    assert Parser(source).parse() == "success"


def test_expr_assignment_chain():
    """73. Assignment chain"""
    source = "void main() { int a; int b; int c; a = b = c = 10; }"
    assert Parser(source).parse() == "success"


def test_expr_struct_init():
    """74. Struct initialization expression"""
    source = "struct Point { int x; int y; }; void main() { Point p = {1, 2}; }"
    assert Parser(source).parse() == "success"


def test_expr_complex():
    """75. Complex expression"""
    source = "void main() { auto x = (a + b) * c - d / e % f && g || !h; }"
    assert Parser(source).parse() == "success"


# Complex/Combined Tests
def test_complete_program_calculator():
    """76. Complete calculator program"""
    source = """
    int add(int x, int y) { return x + y; }
    int sub(int x, int y) { return x - y; }
    void main() { auto a = readInt(); auto b = readInt(); printInt(add(a, b)); }
    """
    assert Parser(source).parse() == "success"


def test_complete_program_factorial():
    """77. Complete factorial program"""
    source = """
    int factorial(int n) {
        if (n <= 1) { return 1; }
        return n * factorial(n - 1);
    }
    void main() { auto n = readInt(); printInt(factorial(n)); }
    """
    assert Parser(source).parse() == "success"


def test_complete_program_struct():
    """78. Complete struct program"""
    source = """
    struct Student { string name; int age; float gpa; };
    void printStudent(Student s) { printString(s.name); printInt(s.age); printFloat(s.gpa); }
    void main() { Student Tan = {"Tan", 22, 3.9}; printStudent(Tan); }
    """
    assert Parser(source).parse() == "success"


def test_complete_program_loop():
    """79. Complete loop program"""
    source = """
    void main() {
        auto sum = 0;
        for (auto i = 1; i <= 100; ++i) { sum = sum + i; }
        printInt(sum);
    }
    """
    assert Parser(source).parse() == "success"


def test_nested_blocks():
    """80. Nested blocks"""
    source = "void main() { { { { auto x = 1; } } } }"
    assert Parser(source).parse() == "success"


# Error Tests - Invalid Syntax
def test_error_missing_function_body():
    """81. Error: missing function body"""
    source = "void main()"
    assert Parser(source).parse() != "success"


def test_error_missing_equals():
    """82. Error: missing equals in initialization"""
    source = "void main() { int x 5; }"
    assert Parser(source).parse() != "success"


def test_error_while_no_paren():
    """83. Error: while without parentheses"""
    source = "void main() { while x < 10 { ++x; } }"
    assert Parser(source).parse() != "success"


def test_error_for_missing_semicolons():
    """84. Error: for without semicolons"""
    source = "void main() { for (auto i = 0 i < 10 ++i) {} }"
    assert Parser(source).parse() != "success"


def test_error_struct_missing_brace():
    """85. Error: struct missing closing brace"""
    source = "struct Tan { int x; int y;"
    assert Parser(source).parse() != "success"


def test_error_case_without_colon():
    """86. Error: case without colon"""
    source = "void main() { switch (x) { case 1 break; } }"
    assert Parser(source).parse() != "success"


def test_error_function_missing_paren():
    """87. Error: function call missing parenthesis"""
    source = "void main() { printInt 5; }"
    assert Parser(source).parse() != "success"


def test_error_unclosed_paren():
    """88. Error: unclosed parenthesis in expression"""
    source = "void main() { auto x = (1 + 2; }"
    assert Parser(source).parse() != "success"


def test_error_struct_member_no_type():
    """89. Error: struct member without type"""
    source = "struct HCMUT { x; y; };"
    assert Parser(source).parse() != "success"


def test_error_default_without_colon():
    """90. Error: default without colon"""
    source = "void main() { switch (x) { default break; } }"
    assert Parser(source).parse() != "success"


def test_error_missing_semicolon():
    """91. Error: missing semicolon"""
    source = "void main() { int x }"
    assert Parser(source).parse() != "success"


def test_error_missing_brace():
    """92. Error: missing closing brace"""
    source = "void main() { int x;"
    assert Parser(source).parse() != "success"


def test_error_missing_paren():
    """93. Error: missing parenthesis in if"""
    source = "void main() { if x > 0 { printInt(x); } }"
    assert Parser(source).parse() != "success"


def test_error_invalid_expression():
    """94. Error: invalid expression"""
    source = "void main() { auto x = + * 5; }"
    assert Parser(source).parse() != "success"


def test_error_missing_struct_semi():
    """95. Error: missing semicolon after struct"""
    source = "struct Point { int x; int y; }"
    assert Parser(source).parse() != "success"


def test_error_invalid_for():
    """96. Error: invalid for statement"""
    source = "void main() { for (auto i = 0 i < 10; ++i) {} }"
    assert Parser(source).parse() != "success"


def test_error_switch_no_brace():
    """97. Error: switch without braces"""
    source = "void main() { switch (x) case 1: break; }"
    assert Parser(source).parse() != "success"


def test_error_double_operator():
    """98. Error: double operator"""
    source = "void main() { auto x = 1 ++ 2; }"
    assert Parser(source).parse() != "success"


def test_error_empty_function_params():
    """99. Error: comma without parameter"""
    source = "void f(int x,) {}"
    assert Parser(source).parse() != "success"


def test_error_invalid_member():
    """100. Error: invalid member access"""
    source = "void main() { auto x = a.; }"
    assert Parser(source).parse() != "success"