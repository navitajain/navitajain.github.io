class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        idx = 1
        op_dict = {'multiply':[N],'divide':[],'add':[]}
        
        #since Python doesnot have switch case statements
        for i in range(N-1,0,-1):
            if idx ==1:
                op_dict['multiply'].append(i)
            elif idx ==2:
                op_dict['divide'].append(i)
            elif idx == 3:
                op_dict['add'].append(i)
            elif idx ==4 :  #substraction taken care
                op_dict['multiply'].append(-i)
                idx = 0
            idx += 1
        
        print(op_dict)
        if len(op_dict['multiply'])%2 ==0:
            m = [op_dict['multiply'][i]*op_dict['multiply'][i+1] for i in range(0,len(op_dict['multiply']),2)]
        else:
            m = [op_dict['multiply'][i]*op_dict['multiply'][i+1] for i in range(0,len(op_dict['multiply'])-1,2)]
            m.append(op_dict['multiply'][-1])
        print('m:', m)
        
        d = [m[i]//op_dict['divide'][i] for i in range(len(op_dict['divide']))]
        if len(d) < len(m):
            d.append(m[-1])
        print('d', d)

        return sum(d)+sum(op_dict['add'])



a = Solution()
print(a.clumsy(10))
print(a.clumsy(5))