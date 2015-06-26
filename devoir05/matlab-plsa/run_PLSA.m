% load the terms by documents matrix
load 4news.txt;
who % lists your variables in the workspace

% call PLSA, searching for 4 topics
[P1,P2]=PLSA(X4news,4);

% here I plot the data and the parameter matrices obtained
% it makes a few lines to make a pretty picture 
% everywhere, darker means higher probability, because I use 1-(the matrix)

subplot(131);imagesc(1-X4news); % this is the input data
ylabel('Terms')
xlabel('Documents')

% now I plot the obtained P1 and P2
subplot(164);imagesc(1-P1);colormap gray;  % this is the topics by terms matrix 
xlabel('Topics')
ylabel('Terms')

subplot(336);imagesc(1-P2);colormap gray  % this is the Documents by topics matrix
ylabel('Topics')
xlabel('Documents')

% now load in the actual list of terms
[ignore, terms]=textread('4news_dictionary.txt','%d %s',-1);

% and now we are certainly set up to solve the exercise
% P1 has the info needed - the probabilities of all terms in all topics. 
% I'll leave it to you to list out the 10 most probable terms.
 
