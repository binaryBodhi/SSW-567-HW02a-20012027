# SSW-567-HW02a

## Test Report 1:

|Test ID|Input|Expected Result|Actual Result|Pass or Fail|
|---|---|---|---|---|
|testRightTriangleA|3, 4, 5|Right|InvalidInput|Fail|
|testRightTriangleB|5, 4, 3|Right|InvalidInput|Fail|
|testEquilateralTriangles|1, 1, 1|Equilateral|InvalidInput|Fail|
|testScaleneTriangle|9, 12, 15|Scalene|InvalidInput|Fail|
|testIsoscelesTriangle|2, 2, 1|Isosceles|InvalidInput|Fail|
|testInvalidInput|‘a’, 2, 1|InvalidInput|TypeError: '>' not supported between instances of 'str' and 'int'|Fail|
|testLengthLimit|201, 9, 100|InvalidInput|InvalidInput|Pass|
|testNegativeInput|-1, 2, -9|InvalidInput|InvalidInput|Pass|
|testForNotATriangle|12, 5, 7|NotATriangle|InvalidInput|Fail|

## Test Report 2:

|Test ID|Input|Expected Result|Actual Result|Pass or Fail|
|---|---|---|---|---|
|testRightTriangleA|3, 4, 5|Right|Right|Pass|
|testRightTriangleB|5, 4, 3|Right|InvalidInput|Fail|
|testEquilateralTriangles|1, 1, 1|Equilateral|Equilateral|Pass|
|testScaleneTriangle|9, 12, 15|Scalene|InvalidInput|Fail|
|testIsoscelesTriangle|2, 2, 1|Isosceles|Isosceles|Pass|
|testInvalidInput|‘a’, 2, 1|InvalidInput|TypeError: '>' not supported between instances of 'str' and 'int'|Fail|
|testLengthLimit|201, 9, 100|InvalidInput|InvalidInput|Pass|
|testNegativeInput|-1, 2, -9|InvalidInput|InvalidInput|Pass|
|testForNotATriangle|12, 5, 7|NotATriangle|NotATriangle|Pass|

## Test Report 3:

|Test ID|Input|Expected Result|Actual Result|Pass or Fail|
|---|---|---|---|---|
|testRightTriangleA|3, 4, 5|Right|Right|Pass|
|testRightTriangleB|5, 4, 3|Right|InvalidInput|Fail|
|testEquilateralTriangles|1, 1, 1|Equilateral|Equilateral|Pass|
|testScaleneTriangle|9, 12, 15|Scalene|InvalidInput|Fail|
|testIsoscelesTriangle|2, 2, 1|Isosceles|Isosceles|Pass|
|testInvalidInput|‘a’, 2, 1|InvalidInput|InvalidInput|Pass|
|testLengthLimit|201, 9, 100|InvalidInput|InvalidInput|Pass|
|testNegativeInput|-1, 2, -9|InvalidInput|InvalidInput|Pass|
|testForNotATriangle|12, 5, 7|NotATriangle|NotATriangle|Pass|

## Test Report 4:

|Test ID|Input|Expected Result|Actual Result|Pass or Fail|
|---|---|---|---|---|
|testRightTriangleA|3, 4, 5|Right|Right|Pass|
|testRightTriangleB|5, 4, 3|Right|Right|Pass|
|testEquilateralTriangles|1, 1, 1|Equilateral|Equilateral|Pass|
|testScaleneTriangle|5, 7, 9|Scalene|Scalene|Pass|
|testIsoscelesTriangle|2, 2, 1|Isosceles|Isosceles|Pass|
|testInvalidInput|‘a’, 2, 1|InvalidInput|InvalidInput|Pass|
|testLengthLimit|201, 9, 100|InvalidInput|InvalidInput|Pass|
|testNegativeInput|-1, 2, -9|InvalidInput|InvalidInput|Pass|
|testForNotATriangle|12, 5, 7|NotATriangle|NotATriangle|Pass|

## Final Report:
||Test Run 1|Test Run 2|Test Run 3|Test Run 4|
|---|---|---|---|---|
|Tests Planned|9|9|9|9|
|Tests Executed|9|9|9|9|
|Tests Passed|2|6|7|9|
|Tests Failed|7|3|2|0|
|Defects Detected|5|1|1|0|
|Defects Fixed|-|5|1|1|

[![binaryBodhi](https://circleci.com/gh/binaryBodhi/SSW-567-HW02a-20012027.svg?style=svg)](https://app.circleci.com/pipelines/github/binaryBodhi/SSW-567-HW02a-20012027?branch=main&filter=all)
