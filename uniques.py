def numUniqueEmails(self, emails) -> int:
        uniques = set()
 
        for mail in emails:
            local, domain = mail.split('@')
            if domain.count(".") == 1:
                local = local.split('+')[0].strip('.')
                final_email = f"{local}@{domain}"
                uniques.add(final_email)
        return len(uniques)    
       