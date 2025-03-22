#include <stdio.h>
void traverse(int arr[], int n) // traverse function define kar rahe hai
{
    for (int i = 0; i < n; i++) // for loop chal rahe hai
    {
        printf("%d\n", arr[i]); // print kar rahe hai
    }
}
int display(int arr[], int n)  // display function define kar rahe hai
{
    int first_element = 0;      // first element ko 0 kar rahe hai
    int second_element = 0;     // second element ko 0 kar rahe hai
    for (int i = 0; i < n; i++) // for loop chal rahe hai
    {
        if (arr[i] > first_element)  // agar array ka element first element se bada hai to
        {
            second_element = first_element;     // second element ko first element me store kar rahe hai
            first_element = arr[i];          // first element ko array ka element me store kar rahe hai
        }
        else if (arr[i] < first_element && arr[i] > second_element)  // agar array ka element first element se chota hai aur second element se bada hai to
        {
            second_element = arr[i]; // second element ko array ka element me store kar rahe hai
        }
    }
    return second_element;  // second element ko return kar rahe hai
}
int main()  // idhar se shuru hota hai
{                                         
    int arr[] = {12, 35, 1, 10, 34, 1};   // 5 elements store kar rahe hai
    int n = sizeof(arr) / sizeof(arr[0]); // sare elements ka size nikal rahe hai
    traverse(arr, n);                     // traverse function call kar rahe hai
    int j = display(arr, n);
    printf("%d\t", j);
    return 0; // return 0 kar rahe hai
}
