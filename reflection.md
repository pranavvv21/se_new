# **Reflection**

1. **Which issues were the easiest to fix, and which were the hardest? Why?**  
   The easiest fixes were the simple ones, like removing the unused import or the eval() line. The hardest was definitely fixing the global variable, as it required restructuring the entire file from functions into a class, which was a big design change.  
2. **Did the static analysis tools report any false positives? If so, describe one example.**  
   No, I didn't run into any false positives. All the reports seemed valid; the eval() function *was* a real security risk, and the "dangerous default value" (logs=\[\]) is a well-known Python bug that can cause a lot of confusion.  
3. **How would you integrate static analysis tools into your actual software development workflow?**  
   I would use them as a "pre-commit hook" in Git. This way, the tools automatically scan my code for any style or security issues right before I commit, forcing me to fix them and preventing bad code from ever getting into the repository.  
4. **What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?**  
   The code is *so* much more robust. We're now catching specific KeyError exceptions instead of just ignoring all errors, and we've removed a major security hole (eval()). Using a class also makes the code much cleaner and easier to read.