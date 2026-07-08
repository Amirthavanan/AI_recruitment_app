import api from "../utils/api";
import type {
    LoginRequest,
    TokenResponse,
} from "../types/auth";

class AuthService {
    async login(
        request: LoginRequest
    ): Promise<TokenResponse> {
        const response = await api.post<TokenResponse>(
            "/auth/login",
            request
        );

        return response.data;
    }
}

export default new AuthService();