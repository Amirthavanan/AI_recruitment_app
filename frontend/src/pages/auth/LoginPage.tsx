import { useState } from "react";
import {
    Alert,
    Box,
    Button,
    Card,
    CardContent,
    CircularProgress,
    Container,
    TextField,
    Typography,
} from "@mui/material";

import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";

import AuthService from "../../services/auth.service";
import { useAuthStore } from "../../store/auth.store";
import type { LoginRequest } from "../../types/auth";

const loginSchema = z.object({
    email: z.email("Enter a valid email address"),
    password: z
        .string()
        .min(8, "Password must be at least 8 characters"),
});

type LoginFormData = z.infer<typeof loginSchema>;

const LoginPage = () => {
    const login = useAuthStore((state) => state.login);

    const [loading, setLoading] = useState(false);

    const [error, setError] = useState("");

    const {
        register,
        handleSubmit,
        formState: { errors },
    } = useForm<LoginFormData>({
        resolver: zodResolver(loginSchema),
    });

    const onSubmit = async (data: LoginRequest) => {
        try {
            setLoading(true);
            setError("");

            const response = await AuthService.login(data);

            login(
                response.access_token,
                response.refresh_token
            );

            alert("Login Successful!");

            console.log(response);

        } catch (err: any) {
            console.error(err);

            setError(
                err?.response?.data?.detail ??
                "Login Failed"
            );
        } finally {
            setLoading(false);
        }
    };

    return (
        <Box
            sx={{
                minHeight: "100vh",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                bgcolor: "#f4f6f8",
            }}
        >
            <Container maxWidth="sm">
                <Card elevation={6}>
                    <CardContent sx={{ p: 5 }}>
                        <Typography
                            variant="h4"
                            align="center"
                            fontWeight="bold"
                            gutterBottom
                        >
                            AI Recruitment Platform
                        </Typography>

                        <Typography
                            align="center"
                            color="text.secondary"
                            sx={{ mb: 4 }}
                        >
                            Sign in to continue
                        </Typography>

                        {error && (
                            <Alert
                                severity="error"
                                sx={{ mb: 2 }}
                            >
                                {error}
                            </Alert>
                        )}

                        <form
                            onSubmit={handleSubmit(onSubmit)}
                        >
                            <TextField
                                fullWidth
                                label="Email"
                                margin="normal"
                                {...register("email")}
                                error={!!errors.email}
                                helperText={
                                    errors.email?.message
                                }
                            />

                            <TextField
                                fullWidth
                                type="password"
                                label="Password"
                                margin="normal"
                                {...register("password")}
                                error={!!errors.password}
                                helperText={
                                    errors.password?.message
                                }
                            />

                            <Button
                                fullWidth
                                type="submit"
                                variant="contained"
                                size="large"
                                sx={{ mt: 3 }}
                                disabled={loading}
                            >
                                {loading ? (
                                    <CircularProgress
                                        size={24}
                                        color="inherit"
                                    />
                                ) : (
                                    "Login"
                                )}
                            </Button>
                        </form>
                    </CardContent>
                </Card>
            </Container>
        </Box>
    );
};

export default LoginPage;