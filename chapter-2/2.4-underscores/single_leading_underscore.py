class SingleLeadingUnderscore:
    def __init__(self):
        self.x = 'regular variable'
        self._y = 'single leading underscore'
        
s = SingleLeadingUnderscore()
print(f'{s.x = }')
# still accessible even with single leading underscore 
print(f'{s._y = }')