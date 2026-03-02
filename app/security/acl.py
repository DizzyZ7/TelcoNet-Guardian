class ACLChecker:
    def validate(self, rules):
        issues = []
        for rule in rules:
            if "deny any any" in rule.lower():
                issues.append("CRITICAL RULE FOUND")
        return issues
