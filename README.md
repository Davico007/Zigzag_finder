# Zigzag_finder
This code checks for the presence of zigzag(s) in an array of numbers

This code checks for the presence of zigzag(s) in an array which would be inputted by the user on prompt. 

A zigzag involves three numbers in an array, [a,b,c], where a<b>c OR a>b<c.

For example, in an array named numbers = [1,2,1,3,4]

It breaks the array down to the different consecutive three items we can get which are [1,2,1], [2,1,3], and [1,3,4]

Each segment returns a value of either 1 or 0 into a new array, depending on if the segment is a zigzag.

 [1,2,1] is a zigzag since 1<2>1. Thus, the segment returns 1.
 
 [2,1,3] is a zigzag since 2>1<3. Thus, the segment returns 1.
 
 [1,3,4] is not zigzag since 1<3<4. Thus, the segment returns 0.

The newly created array will then be [1,1,0], which will be displayed on the console.
