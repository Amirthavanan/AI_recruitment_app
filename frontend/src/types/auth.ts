export interface LoginRequest {
    email: string;
    password: string;
}

export interface TokenResponse {
    access_token: string;
    refresh_token: string;
    token_type: string;
}

export interface User {
    id: string;
    employee_id: string;
    first_name: string;
    last_name: string;
    email: string;
    phone?: string;
    organization_id: string;
    department_id?: string;
}