class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        distance_traveled = 0
        if mainTank < 5:
            distance_traveled = mainTank * 10
        else:
            while mainTank > 0:
                if additionalTank >= 1 and mainTank >= 5:
                    mainTank = mainTank - 4
                    additionalTank -= 1
                    distance_traveled += 50
                else:
                    distance_traveled += mainTank * 10
                    mainTank = 0

        return distance_traveled
