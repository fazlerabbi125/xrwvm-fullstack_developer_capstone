import "./App.css";
import LoginPanel from "./components/Login/Login"
import RegisterPage from "./components/Register/Register";
import { Routes, Route } from "react-router-dom";
import Dealers from './components/Dealers/Dealers';
import DealerDetails from "./components/Dealers/Dealer"

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />
      <Route path="/register" element={<RegisterPage />} />
      <Route path="/dealers" element={<Dealers/>} />
      <Route path="/dealer/:id" element={<DealerDetails/>} />
    </Routes>
  );
}
export default App;
