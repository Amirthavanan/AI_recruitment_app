import { create } from "zustand";
import type { User } from "../types/auth";

interface AuthState {
    user: User | null;
    accessToken: string | null;
    refreshToken: string | null;
    isAuthenticated: boolean;

    login: (
        accessToken: string,
        refreshToken: string
    ) => void;

    logout: () => void;
}

export const useAuthStore = create<AuthState>((set) => ({
    user: null,

    accessToken: localStorage.getItem("access_token"),

    refreshToken: localStorage.getItem("refresh_token"),

    isAuthenticated: !!localStorage.getItem("access_token"),

    login: (accessToken, refreshToken) => {
        localStorage.setItem("access_token", accessToken);
        localStorage.setItem("refresh_token", refreshToken);

        set({
            accessToken,
            refreshToken,
            isAuthenticated: true,
        });
    },

    logout: () => {
        localStorage.removeItem("access_token");
        localStorage.removeItem("refresh_token");

        set({
            user: null,
            accessToken: null,
            refreshToken: null,
            isAuthenticated: false,
        });
    },
}));