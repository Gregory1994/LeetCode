/*
 * @lc app=leetcode.cn id=58 lang=cpp
 *
 * [58] 最后一个单词的长度
 *
 * https://leetcode-cn.com/problems/length-of-last-word/description/
 *
 * algorithms
 * Easy (28.96%)
 * Total Accepted:    21.5K
 * Total Submissions: 73.6K
 * Testcase Example:  '"Hello World"'
 *
 * 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
 * 
 * 如果不存在最后一个单词，请返回 0 。
 * 
 * 说明：一个单词是指由字母组成，但不包含任何空格的字符串。
 * 
 * 示例:
 * 
 * 输入: "Hello World"
 * 输出: 5
 * 
 * 
 */
class Solution {
public:
    int lengthOfLastWord(string s) {
        int index = s.size() - 1;
        int len = 0;
        while(s[index] == ' ' & index >= 0) index--;
        while(s[index] != ' ' & index >= 0){
            len++;
            index--;
        }
        return len; 
        
    }
};

