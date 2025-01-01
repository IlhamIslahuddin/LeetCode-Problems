class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        def invert(new_image):
            n = len(new_image)
            for i in range (n):
                for j in range(n):
                    if new_image[i][j] == 0:
                        new_image[i][j] = 1
                    else:
                        new_image[i][j] = 0
            return new_image
        def flip_hori(new_image):
            n = len(new_image)
            for i in range (n):
                for j in range(n // 2):
                    temp = new_image[i][j]
                    new_image[i][j] = new_image[i][n-1-j]
                    new_image[i][n-1-j] = temp
            return new_image
        new = flip_hori(image)
        return invert(new)
