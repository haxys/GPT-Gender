# The Gender Calculator

**DISCLAIMER: This is not intended to be used as a scientific tool. It is just for fun. Any sudden self-discoveries should be explored with a trained professional.**

I asked ChatGPT to describe the common qualities and traits associated with masculinity and femininity in the United States. I then asked it to score those traits based on how masculine or feminine they are. I then used this data to create a very simple, very unscientific survey, which you can use to calculate your very own gender score!

Unfortunately, it's based on societal views, which fall along a Male/Female spectrum. This fails to account for non-binary, genderqueer, and other identities. Further research should be conducted to create a more inclusive version of this calculator.

## Conversational Foundation

* [Gender Norms in America](https://chat.openai.com/share/8a7235c1-f3d8-4562-b44f-98f083b24e25)
    * Collecting basic information about gender norms and perceptions.
* [Gender Norms Overview](https://chat.openai.com/share/1ae8a624-907b-42c8-b929-994cb6853621)
    * Breaking down the collected information into (highly subjective) numerical scores.
    * Note: I removed any elements from the list that had a score of 0.0, as these had no weight in the final calculation.

## Testing the LLMs' Genders
* [GPT-3.5 Interview](responses/gpt3.md)
    * A conversation with GPT-3.5 wherein we determine who they would be, were they a human.
* [GPT-4 Interview](responses/gpt4.md)
    * A conversation with GPT-4 wherein we determine who they would be, were they a human.

Tool output:

```
kris10hax@madlab Gender % ./calculate.py responses/*.json
[max_masc] Score: 0.0000            (M ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱ F :: 100% Masculine)
[max_femme] Score: 1.0000           (M ▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰ F :: 100% Feminine)
[responses/gpt3.json] Score: 0.5740 (M ▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▱▱▱▱▱▱▱▱▱▱▱▱ F :: 57% Feminine)
[responses/gpt4.json] Score: 0.5222 (M ▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱ F :: 52% Feminine)
```