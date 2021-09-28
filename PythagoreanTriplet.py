def PythogoreanTriple(N):
     for a in range(1, 400):
        for b in range(1, 400):
        
            # Find c bysubstracting a and b from 1000
            # There is no need to loop for c.
            c = (N - a) - b
        
            # each number must be smaller than the next
            if a < b < c:
            
                # check if numbers are pythagorean triplet
                if a**2 + b**2 == c**2:
                
                    # calculate the product
                    print(a * b * c)
PythogoreanTriple(1000)                    