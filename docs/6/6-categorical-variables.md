# 6-categorical-variables.md

- Some of your features may be discrete values that aren’t in an ordered relationship. Examples include breeds of dogs, words, or postal codes. These features are known as categorical and each value is called a category. You can represent categorical values as strings or even numbers, but you won't be able to compare these numbers or subtract them from each other.
- Oftentimes, you should represent features that contain integer values as categorical data instead of as numerical data. For example, consider a postal code feature in which the values are integers. If you mistakenly represent this feature numerically, then you're asking the model to find a numeric relationship between different postal codes; for example, you're expecting the model to determine that postal code 20004 is twice (or half) the signal as postal code 10002. By representing postal codes as categorical data, you enable the model to find separate signals for each individual postal code.
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 