class Solution {
    public boolean isAnagram(String s, String t) {
        // we can use a hashMap and go through the letters 
        // check if the length of the two strings are different first
        if (s.length() != t.length()) {
            return false;
        }

        // create a hashMap to store s and t
        HashMap <Character, Integer> hashMapS = new HashMap<>();
        HashMap <Character, Integer> hashMapT = new HashMap<>();

        // go through string S and start storing the letters
        for (int i = 0; i < s.length(); i++) {
            // we want to store the string's letter and count into the map
            hashMapS.put(s.charAt(i), hashMapS.getOrDefault(s.charAt(i),0) + 1);
            hashMapT.put(t.charAt(i), hashMapT.getOrDefault(t.charAt(i),0) + 1);
        }

        return hashMapT.equals(hashMapS);

    

    }
}
