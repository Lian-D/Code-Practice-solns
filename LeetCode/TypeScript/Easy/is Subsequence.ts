//Runtime: 65 ms, faster than 97.99% of TypeScript online submissions for Is Subsequence.
//Memory Usage: 43 MB, less than 67.11% of TypeScript online submissions for Is Subsequence.

function isSubsequence(s: string, t: string): boolean {
    let sIndex = 0;
    for (let i = 0; i < t.length; i++) {
        if (s.charAt(sIndex) == t.charAt(i)) {
            sIndex++;
        }
    }
    if (sIndex == s.length) {
        return true;
    } else {
        return false;
    }
};
