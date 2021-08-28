import React, { ReactElement } from 'react';

import { Wrapper, MainWrapper, MainArticle } from './main.styles';

const Main = (): ReactElement => {
  return (
    <Wrapper>
      <MainWrapper>
        <MainArticle>123</MainArticle>
      </MainWrapper>
    </Wrapper>
  );
};

export default Main;
