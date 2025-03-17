class Solution(object):
    def floodFill(self, image, sr, sc, color):
        changecolor = image[sr][sc]
        if changecolor == color: return image
        
        def fill(sr, sc):
            if (image[sr][sc] == changecolor):
                image[sr][sc] = color
                if sr > 0:
                    fill(sr-1, sc)
                if sc > 0:
                    fill(sr, sc-1)
                if sr+1 < len(image):
                    fill(sr+1, sc)
                if sc+1 < len(image[0]):
                    fill(sr, sc+1)
        fill(sr, sc)
        return image
        