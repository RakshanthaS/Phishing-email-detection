Our approach performs a semantic analysis of the text of email to verify the appropriateness of each sentence.

A sentence is considered to be malicious if it inquires sensitive information or commands an action.

NLP techniques are used to parse each sentence and identify the semantic roles of  words in a sentence in relation to the predicate.

Identification of malicious commands and questions depends on the existence of Topic blacklist which is a list of verb - direct object pair.

Topic Blacklist is a list of verb - direct object pairs whose presence in a question indicate malicious intent.

Naive bayes classifier is used to create topic blacklist.

We used the spacy dependency parser to extract all verb -object pair from datasets (phishing and non phishing)

These pairs are the features extracted and is given for training.

After training , we considered a pair to malicious if it exceeded a threshold(in our case 0.9)

260 verb direct object pairs were collected.(Click here, disable account, send money)
