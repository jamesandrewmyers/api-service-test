import json
import logging
from typing import Dict, Any

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    AWS Lambda handler for API service endpoints - test change text
    """
    try:
        logger.info("EVENT: %s", event)
        http_method = event.get('httpMethod', '')
        path = event.get('path', '')
        
        if path == '/getById' and http_method == 'GET':
            return handle_get_by_id(event)
        elif path == '/upsert' and http_method == 'POST':
            return handle_upsert(event)
        elif path == '/delete' and http_method == 'DELETE':
            return handle_delete(event)
        else:
            return create_response(404, {'error': 'Endpoint not found'})
    
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return create_response(500, {'error': 'Internal server error'})


def handle_get_by_id(event: Dict[str, Any]) -> Dict[str, Any]:
    """
    Handle GET /getById endpoint
    Requires an integer parameter 'id'
    """
    query_params = event.get('queryStringParameters') or {}
    id_param = query_params.get('id')
    
    if id_param is None:
        return create_response(400, {'error': 'Missing required parameter: id'})
    
    try:
        id_value = int(id_param)
        return create_response(200, {'id': id_value})
    except ValueError:
        return create_response(400, {'error': 'Parameter id must be a valid integer'})


def handle_upsert(event: Dict[str, Any]) -> Dict[str, Any]:
    """
    Handle POST /upsert endpoint
    Requires JSON body with 'id' attribute containing a valid integer
    """
    try:
        body = event.get('body', '')
        if not body:
            return create_response(400, {'error': 'Request body is required'})
        
        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            return create_response(400, {'error': 'Invalid JSON in request body'})
        
        if 'id' not in data:
            return create_response(400, {'error': 'Missing required attribute: id'})
        
        try:
            int(data['id'])
        except (ValueError, TypeError):
            return create_response(400, {'error': 'Attribute id must be a valid integer'})
        
        return create_response(200, {'message': 'Success'})
    
    except Exception as e:
        logger.error(f"Error in upsert: {str(e)}")
        return create_response(500, {'error': 'Internal server error'})


def handle_delete(event: Dict[str, Any]) -> Dict[str, Any]:
    """
    Handle DELETE /delete endpoint
    Requires an integer parameter 'id'
    """
    query_params = event.get('queryStringParameters') or {}
    id_param = query_params.get('id')
    
    if id_param is None:
        return create_response(400, {'error': 'Missing required parameter: id'})
    
    try:
        int(id_param)
        return create_response(200, {'message': 'Success'})
    except ValueError:
        return create_response(400, {'error': 'Parameter id must be a valid integer'})


def create_response(status_code: int, body: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create a standardized API response
    """
    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(body)
    }
