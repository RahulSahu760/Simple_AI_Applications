from transformers import AutoTokenizer, AutoModelForSeq2SeqLM #tokenizer prepares the input text, AutoModelForSeq2SeqLM loads the model

model_name = "facebook/blenderbot-400M-distill"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

conversation_history = []

def generate_response(input_text):
    global conversation_history

    history_string = "\n".join(conversation_history)# so if you have a list of strings, you can join them into a single string or else you can use tradional way : for line in conv_hist: print(line)
    try: 
        inputs = tokenizer.encode_plus(history_string, input_text, return_tensors="pt")# combines previous conversation + current input and converts to model understandable format. return_tensors="pt" means return pytorch tensor
        outputs = model.generate(**inputs)

        response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
        print(response)

        conversation_history.append(input_text)
        conversation_history.append(response)

        return conversation_history
    except Exception as e:
        print(e)
        return {"error": str(e)}
