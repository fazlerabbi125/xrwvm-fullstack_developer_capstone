import LoginPanel from "./components/Login/Login"
import RegisterPage from "./components/Register/Register";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />
      <Route path="/register" element={<RegisterPage />} />
    </Routes>
  );
}
export default App;
