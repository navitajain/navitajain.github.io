

class Solution(object):
	def greaterNum(self,n):

		num = [i for i in n]
		grt_num = []
		# descending integer list
		des_num = sorted(num)[::-1]

		lptr = 0
		rptr = 1

		while num[lptr] > num[rptr]:
			grt_num.append(des_num.pop(des_num.index(num[lptr])))
			lptr = lptr+1
			rptr = rptr+1
			if rptr == len(num):
				return "Not Possible"
		grt_num.append(des_num.pop(des_num.index(num[lptr])-1))
		grt_num += [i for i in des_num[::-1]]

		return ''.join([str(a) for a in grt_num])
		#return grt_num

a = Solution()
print(a.greaterNum('534976'))

