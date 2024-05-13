#https://leetcode.com/problems/two-sum/description/
#Pull request用の書き込み

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        flag = False
        num_L = []
        for i in range(0,len(nums)-1):
            for j in range(0,len(nums)-1):
                if nums[i] +  nums[j] == nums[len(nums)-1]:
                    num_L.append(nums[i])
                    num_L.append(nums[j])
                    flag = True
                    print(num_L)
                    break
            if flag:
                break

#10minでここまで書いた　エラーが出てしまった

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        flag = False
        num_L = []
        for i in range(0,len(nums)-1):
            for j in range(0,len(nums)-1):
                if nums[i] +  nums[j] == nums[len(nums)-1]:
                    num_L.append(nums[i])
                    num_L.append(nums[j])
                    flag = True
                    print(num_L)
                    break
            if flag:
                break

#15minで書き直してacceptされた。Leetcodeの使い方とこのー＞の書き方に慣れていませんでした。
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        flag = False
        num_L = []
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if nums[i] +  nums[j] == target:
                    if i != j:
                        flag = True
                        return(i,j)
                        break
            if flag:
                break

#答えを送信して、正解になったら、まずは一段階目です。次にコードを読みやすくするようにできるだけ整えましょう。
#これで動くコードになったら二段階目です。そしたららまた全部消しましょう。

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        flag = False
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if nums[i] +  nums[j] == target:
                    if i != j:
                        flag = True
                        return(i,j)
                        break
            if flag:
                break

# num_L = []という余計な行を上記から消しました。

#今度は、時間を測りながら、もう一回、書きましょう。書いてアクセプトされたら文字消してもう一回書きましょう。
#これを10分以内に一回もエラーを出さずに書ける状態になるまで続けてください。
#3回続けてそれができたらその問題はひとまず丸です。

#error あり　2
#error なし　2
#error あり　2
#error なし　3

#コメント
#ロジックを思いつくところまではすぐ行きましたが、細かいスペルミスがあったりして3連続正解を書くのは苦労しました。
#最終コードは下記です。

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     flag = False
     for i in range(0,len(nums)):
        for j in range(0,len(nums)):
            if nums[i] + nums[j] == target and i != j:
                flag = True
                return i,j
                break
        if flag:
            break

#書き直し

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     flag = False
     nums2 = sorted(nums)
     #nums.sort()
     
     j = len(nums2) - 1
     i = 0
     print(nums[i+1:])
     while  nums2[i] + nums2[j] > target and j > 0:
        j = j - 1
     while  nums2[i] + nums2[j] < target and i < len(nums2)-1:
        i = i + 1
     if nums2[i] + nums2[j] == target and i != j:
        flag = True
        return nums.index(nums2[i]),nums[i+1:].index(nums2[j]) + 1
     
#コードの整理

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2 = sorted(nums)  
        j = len(nums2) - 1
        i = 0
        while nums2[i] + nums2[j] > target and j > 0:
            j = j - 1
        while nums2[i] + nums2[j] < target and i < len(nums2) - 1:
            i = i + 1
        if nums2[i] + nums2[j] == target and i != j:
            return nums.index(nums2[i]), nums[i + 1:].index(nums2[j]) + 1

#アルゴリズム書き直し　submitしてacceptされました。43ms ※コピペし直し

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2 = sorted(nums)  
        j = len(nums2) - 1
        i = 0
        while nums2[i] + nums2[j] != target or i == j:
            if nums2[i] + nums2[j] == target and i == j:
                if j > 0:
                    j = j - 1
                else:
                    i = i + 1
            if nums2[i] + nums2[j] > target and j > 0:
                j = j - 1
            if nums2[i] + nums2[j] < target and i < len(nums2) - 1:
                i = i + 1
            
        if nums2[i] + nums2[j] == target and i != j:
            if nums2[i] == nums2[j]:
                l = [c for c, x in enumerate(nums) if x == nums2[i]]
                return l[0], l[1]
            else:
                return nums.index(nums2[i]), nums.index(nums2[j])
            

#答えを送信して、正解になったら、まずは一段階目です。次にコードを読みやすくするようにできるだけ整えましょう。
#これで動くコードになったら二段階目です。そしたららまた全部消しましょう。
    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2 = sorted(nums)  
        j = len(nums2) - 1
        i = 0
        while nums2[i] + nums2[j] != target:
            if nums2[i] + nums2[j] > target and j > 0:
                j = j - 1
            if nums2[i] + nums2[j] < target and i < len(nums2) - 1:
                i = i + 1
        if nums2[i] == nums2[j]:
            l = [c for c, x in enumerate(nums) if x == nums2[i]]
            return l[0], l[1]
        else:
            return nums.index(nums2[i]), nums.index(nums2[j])

#答えを送信して、正解になったら、まずは一段階目です。次にコードを読みやすくするようにできるだけ整えましょう。
#これで動くコードになったら二段階目です。そしたららまた全部消しましょう。

#いただいたコメントを元に最適化　39MSで99.81%をbeatsするコードになりました。

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2 = sorted(nums)  
        i = 0
        j = len(nums2) - 1
        while nums2[i] + nums2[j] != target:
            if nums2[i] + nums2[j] > target:
                j = j - 1
            if nums2[i] + nums2[j] < target:
                i = i + 1
        if nums2[i] == nums2[j]:
            l = [c for c, x in enumerate(nums) if x == nums2[i]]
            return l[0], l[1]
        else:
            return nums.index(nums2[i]), nums.index(nums2[j])