# API Warm-up Results

## The request

I sent the URL https://api.anthropic.com/v1/messages
The three headers:

-H "x-api-key: $ANTHROPIC_API_KEY" \
 -H "anthropic-version: 2023-06-01" \
 -H "content-type: application/json" \

What each one is for:

- x-api-key: who I am, and who gets billed.
- anthropic-version: which version of the API rules I expect.
- content-type: tells the server the body is JSON.

And the JSON body
-d '{"model":"'"$MODEL_ID"'","max_tokens":100,"messages":[{"role":"user","content":"Say hello in five words."}]}' | jq

## The response

{
"model": "claude-haiku-5-5",
"id": "msg_011Cg6TT8ZnQEyzKMmZnZWQB",
"type": "message",
"role": "assistant",
"content": [
{
"type": "text",
"text": "Hello there, friend! Welcome aboard."
}
],
"container": null,
"stop_reason": "end_turn",
"stop_sequence": null,
"stop_details": null,
"usage": {
"input_tokens": 16,
"cache_creation_input_tokens": 0,
"cache_read_input_tokens": 0,
"cache_creation": {
"ephemeral_5m_input_tokens": 0,
"ephemeral_1h_input_tokens": 0
},
"output_tokens": 18,
"output_tokens_details": {
"thinking_tokens": 0
},
"service_tier": "standard",
"inference_geo": "global",
"speed": "standard"
},
"diagnostics": null
}

## Three errors

1. Bad API Key
   anthropic.AuthenticationError: Error code: 401 - {'type': 'error', 'error': {'type': 'authentication_error', 'message': 'invalid x-api-key'}, 'request_id': 'req_011Cg6Scqo8iHuRQvwVqWu1j'}

2. Delete max_tokens
   TypeError: Missing required arguments; Expected either ('max_tokens', 'messages' and 'model') or ('max_tokens', 'messages', 'model' and 'stream') arguments to be given

3. Bogus model
   anthropic.NotFoundError: Error code: 404 - {'type': 'error', 'error': {'type': 'not_found_error', 'message': 'model: claude-haik-5-5'}, 'request_id': 'req_011Cg6SqV3aRcytSgs6gwG1q'}

## What I'll do differently in the real tool

- Load the API key from the environment, never from code.
- Double-check the model name, because a typo gives a 404.
- Check stop_reason, and use the template summary if it isn't end_turn.
- Keep counts and ordering in plain code, not model output.
