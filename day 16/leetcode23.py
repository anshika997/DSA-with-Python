# This function converts a valid IP address into a defanged IP address.
# Defanging means replacing every '.' with '[.]' to prevent misuse.
# We traverse the string character by character.
# If the character is '.', we append '[.]' to the result string.
# Otherwise, we append the character as it is.
# Finally, we return the defanged IP address.

class solution:
    def defangIpaddr(self,address:str)->str:
        return address.replace(".","[.]")
sol=solution()
print(sol.defangIpaddr("1.1.1.1"))


 
# class solution:
#     def defangIpaddr(self,address:str)->str:
#         ans =""
#         for i in address:
#             if i==".":
#                 ans+="[.]"
#             else:
#                 ans+=i
#         return ans

    
# class solution:
#     def defangIpaddr(self,address:str)->str:
#         ans =""
#         for i in address:
#             if i!=".":
#                 ans+=i
#             else:
#                 ans+="[.]"
#         return ans
# sol=solution()
# print(sol.defangIpaddr("1.1.1.1"))