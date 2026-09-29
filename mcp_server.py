import sys
import json
from client import PersonaEntityStateTracker

tracker = PersonaEntityStateTracker()

def handle_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-agent-persona-entity-state-tracker-skill", "version": "1.0.0"}
            }
        }
    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "update_user_slot",
                        "description": "Update specific profile slot in persona state",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "slot_name": {"type": "string"},
                                "value": {"type": "string"}
                            },
                            "required": ["slot_name", "value"]
                        }
                    },
                    {
                        "name": "add_entity_relation",
                        "description": "Add entity relation triple to graph",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "entity_a": {"type": "string"},
                                "relation": {"type": "string"},
                                "entity_b": {"type": "string"}
                            },
                            "required": ["entity_a", "relation", "entity_b"]
                        }
                    },
                    {
                        "name": "get_persona_state",
                        "description": "Get current persona profile and relation state",
                        "inputSchema": {"type": "object", "properties": {}}
                    }
                ]
            }
        }
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        
        if tool_name == "update_user_slot":
            tracker.update_slot(args.get("slot_name"), args.get("value"))
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": "Slot updated"}]}}
        elif tool_name == "add_entity_relation":
            tracker.add_relation(args.get("entity_a"), args.get("relation"), args.get("entity_b"))
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": "Relation stored"}]}}
        elif tool_name == "get_persona_state":
            st = tracker.get_state()
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(st)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}
            sys.stdout.write(json.dumps(err) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
