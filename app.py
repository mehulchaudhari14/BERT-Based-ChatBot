import json
import time
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

def load_bert_model():
    """
    Mock function to represent loading the optimizer.pt / BERT model.
    """
    model_path = "optimizer.pt"
    if os.path.exists(model_path):
        print(f"Loading {model_path} ... (Mock representation)")
    else:
        print(f"{model_path} not found. Mock running anyway.")
    
    return lambda text: "Predicting intent for: " + text

# "Load" model once at startup
bert_predictor = load_bert_model()

def load_intents():
    if os.path.exists('intents.json'):
        with open('intents.json', 'r') as f:
            return json.load(f)
    return {}

INTENT_DATA = load_intents()

class ChatRequestHandler(BaseHTTPRequestHandler):
    def end_headers(self):
        # Enable CORS for the UI
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
            
        try:
            content_type = 'text/html'
            if self.path.endswith('.css'):
                content_type = 'text/css'
            elif self.path.endswith('.js'):
                content_type = 'application/javascript'
                
            with open(self.path[1:], 'rb') as file:
                content = file.read()
                self.send_response(200)
                self.send_header('Content-Type', content_type)
                self.end_headers()
                self.wfile.write(content)
        except Exception:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == '/api/chat':
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            
            try:
                req_data = json.loads(body.decode('utf-8'))
                user_message = req_data.get('message', '')
                
                # Simulate processing time
                time.sleep(1.2)
                
                # NOTE: Here is where you will eventually put your PyTorch `optimizer.pt` code logic!
                intent_guess = "default"
                answer = "I mapped your intent but don't have a specific answer for it yet. Try asking about weather, bank balance, or status."
                
                # Reload intents per request so you can update intents.json dynamically without restarting!
                import random
                current_intents = load_intents()
                
                # Setup default fallback
                fallback_pool = current_intents.get("fallback", ["I mapped your intent but don't have a specific answer for it yet. Try asking about weather, bank balance, or status."])
                answer = random.choice(fallback_pool) if isinstance(fallback_pool, list) else fallback_pool

                # Mock matching logic since we don't have PyTorch plugged in yet
                msg_lower = user_message.lower()
                for intent_name, responses in current_intents.items():
                    intent_words = intent_name.split('_')
                    
                    # Heuristics for basic simulation testing
                    is_match = False
                    msg_clean = msg_lower.strip()
                    if "hi" in msg_clean or "hello" in msg_clean:
                        if intent_name == "greeting": is_match = True
                    elif "bye" in msg_clean:
                        if intent_name == "goodbye": is_match = True
                    elif msg_clean in ["ok", "okay", "okie", "k", "yes", "sure", "yep", "yeah"]:
                        if intent_name == "yes": is_match = True
                    elif any(w.lower() in msg_clean for w in intent_words if len(w) > 3):
                        is_match = True
                        
                    if is_match:
                        intent_guess = intent_name
                        answer = random.choice(responses) if isinstance(responses, list) else responses
                        break

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                
                res = json.dumps({
                    "intent": intent_guess,
                    "answer": answer
                })
                self.wfile.write(res.encode('utf-8'))
                
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(str(e).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=ChatRequestHandler, port=8000):
    server_address = ('127.0.0.1', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting lightweight server on http://127.0.0.1:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
