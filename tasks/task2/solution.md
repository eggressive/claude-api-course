# Solution

1. Uses message prefilling: Adds an assistant message with "```\n" to establish the format for code blocks
2. Uses stop sequences: Stops generation at the closing \``` to get exactly 3 commands
3. No comments or explanation: Just the AWS CLI commands in the output

The key technique here is:

- Message prefilling: We add an assistant message prefix ("```\n") which guides Claude to continue in that format
- Stop sequences: We tell the API to stop when it hits another set of backticks, so we get exactly the commands without extra text
