//Runtime: 133 ms, faster than 34.96% of TypeScript online submissions for Isomorphic Strings.
//Memory Usage: 45.6 MB, less than 48.78% of TypeScript online submissions for Isomorphic Strings.

function isIsomorphic(s: string, t: string): boolean {
    let letterHash1: Map<string, string> = new Map();
    let letterHash2: Map<string, string> = new Map();

    for (let i = 0; i < s.length; i++) {
        if (letterHash1.get(t.charAt(i)) == undefined && letterHash2.get(s.charAt(i)) == undefined) {
            letterHash1.set(t.charAt(i), s.charAt(i));
            letterHash2.set(s.charAt(i), t.charAt(i));
        } else if (letterHash1.get(t.charAt(i)) != s.charAt(i) || letterHash2.get(s.charAt(i)) != t.charAt(i)) {
            return false
        }
    }
    return true;

};
