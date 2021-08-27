import React, { ReactElement } from 'react';
import { BrowserRouter } from 'react-router-dom';
import { ThemeProvider } from 'styled-components';

import Routes from './Routes';
import GlobalStyle from '../styles/global';
import { theme } from '../styles/theme';

const App = (): ReactElement => (
  <ThemeProvider theme={theme}>
    <BrowserRouter>
      <Routes />
    </BrowserRouter>
    <GlobalStyle />
  </ThemeProvider>
);

export default App;
