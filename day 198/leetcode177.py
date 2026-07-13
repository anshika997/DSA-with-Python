class Solution:
    def numUniqueEmails(self, emails): 
        unique = set ()
        for email in emails :
            parts = email.split('@')
            local = parts[0]
            domain = parts[1]
            local = local.replace('.',"")
            if '+' in local :
                index = local.find("+")
                local = local[:index]
            new_email = local + "@" + domain
            unique.add(new_email)
        return len(unique)
Solution = Solution()
print(Solution.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
print(Solution.numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))