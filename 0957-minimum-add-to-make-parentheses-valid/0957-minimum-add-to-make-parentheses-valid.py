class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        closedstack=0
        openstack=0
        total=0
        for i in s:
            if i =="(":
                # if closedstack != 0:
                #     total+=1
                openstack+=1
            else:
                if openstack == 0:
                    total+=1
                else:
                    # closedstack+=1
                    openstack-=1
                    

        return abs(total+openstack)