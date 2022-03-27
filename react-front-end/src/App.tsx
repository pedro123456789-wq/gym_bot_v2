import {
  BrowserRouter,
  Route,
  Routes,
  Outlet
} from "react-router-dom";
import FeaturesPage from "./Components/FeaturesPage/FeaturesPage";
import LandingPage from './Components/LandingPage/LandingPage';
import LoginPage from "./Components/LoginPage/LoginPage";
import SignUpPage from "./Components/SignUpPage/SignUpPage";


function App(): JSX.Element {
  return (
    <BrowserRouter>
      <div className="App">
        <Routes>
          <Route path = '/' element = {<LandingPage />} />
          <Route path = '/log-in' element = {<LoginPage />} />
          <Route path = '/sign-up' element = {<SignUpPage />} />
          <Route path = '/features' element = {<FeaturesPage />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
