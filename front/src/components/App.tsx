import React, { ReactElement } from 'react';
import { BrowserRouter } from 'react-router-dom';

import Routes from './Routes';

const App = (): ReactElement => (
  <BrowserRouter>
    <Routes />
  </BrowserRouter>
);

export default App;
