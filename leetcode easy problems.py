#9. palindrome number
class Solution(object):
    def isPalindrome(self, x):
        x=str(x)
        reverse=x[::-1]
        if reverse==x:
            return True
        return False

        """
        :type x: int
        :rtype: bool
        """

#14. Longest Common Prefix
class Solution(object):
    def longestCommonPrefix(self, strs):
        out=""
        shortest=min(strs, key=len)
        for i in range(len(shortest)):
            check=0
            for words in strs:
                if words[i]==strs[0][i]:
                    check+=1
            if check!=len(strs):
                break
            else:
                out+=strs[0][i]
        return out
        """
        :type strs: List[str]
        :rtype: str
 
               """
#2729. Check if The Number is Fascinating
class Solution(object):
    def isFascinating(self, n):
        string1=str(n*2)
        string2=str(n*3)
        string=str(n)+string1+string2
        if sorted(string)==['1', '2', '3', '4','5', '6', '7', '8','9']:
            return True
        return False
        """
        :type n: int
        :rtype: bool
        """