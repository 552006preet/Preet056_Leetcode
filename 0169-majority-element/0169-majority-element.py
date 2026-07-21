class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #using Moore-Voting Algorithm
        #by checking the contunity of element and increading the count if another element comes count-=1
        #at the end if count!=0 and count is >len(nums)//2 so that is the majority element
        element=0
        count=0
        for i in nums:
            if count==0:
                count=1
                element=i
            elif i==element:
                count+=1
            else:
                count-=1
        for i in nums:
            if element==i:
                count+=1
        if count>len(nums)//2:
            return element
        return -1

     #another one is there 
     # we have to only write:-
     #return (sorted(nums)[len(nums)//2])
     #by doing this we're just sorting the elements and accessing them and comparing them as >n/2

        