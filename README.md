Problem: Nested List Transformation
You are given a nested list (a list containing other lists) where each inner list contains a mix of integers and strings. Your task is to write a function transform_nested_list(lst) that modifies the given list in the following way:

Remove all strings from each inner list.
Square all the integers present in the inner lists.
If an inner list becomes empty after the transformation (because it contained only strings), remove that inner list from the outer list.
Return the transformed list.
Input:
A list lst, where each element is a list of integers and strings.
Example: [[2, 'a', 3], ['b', 5, 6], ['x', 'y'], [7]]
Output:
A transformed list where:
All strings are removed.
All integers are squared.
Empty inner lists are removed.
Example output for the above input: [[4, 9], [25, 36], [49]]
