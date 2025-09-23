#include <stdio.h>
#include <stdlib.h>
int*duplicates(int arr[], int n, int* result_size) {
 int*ans=NULL;
 int i;
 // Sorting the array
 for(i=0;i<n-1;i++) {
 for (intj=i+1;j<n;j++) {
 if (arr[i]>arr[j]) {
 int temp=arr[i];
 arr[i]=arr[j];
 arr[j]=temp;
 }
 }
 }
 // Finding duplicates
 for (i=1;i<n;i++) {
 if (arr[i]==arr[i-1]&&arr[i]!=arr[i+1]) {
 // Adding the duplicate element to the ans array
 (*result_size)++;
 ans=(int*)realloc(ans,(*result_size)*sizeof(int));
 ans[(*result_size)-1]=arr[i];
 }
 }
 if (*result_size) {
 return ans;
 } else {
 free(ans);
 return NULL;
 }
}
int main()
{
 int num;
 int arr[10];
 printf("enter the number of ids:");
 scanf("%d",&num);
 printf("Enter the id's:");
 for(int i=0;i<num;i++)
 {
 scanf("%d",&arr[i]);
 }
 //int n = sizeof(arr) / sizeof(arr[0]);
 int result_size = 0;
 int*result=duplicates(arr,num,&result_size);
 if (result!=NULL) {
 printf("Duplicate elements are: ");
 for (int i = 0; i < result_size; i++) {
 printf("%d ", result[i]);
 }
 free(result);
 } else {
 printf("-1");
 }
 return 0;
}
