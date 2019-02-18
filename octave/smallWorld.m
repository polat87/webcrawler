%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%					   		 Small World							   %
%						GOEKHAN POLAT (0830690)						   %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% TODO: implement a function that calculates the average path length L and the clustering coefficient C
% INPUT: adjacency matrix (nxn) of the one-mode network
% OUTPUT: L and C value (doubles)
function [L, C] = smallWorld(network)
    M = zeros(size(network)(1),size(network)(1));

    for i=1:size(network)(1);
        M+=(M<=0).*(network^i>0).*i;

    M(1:(size(network)+1):size(network)(1)*size(network)(2)) = 0;
    L = sum(sum(M))/(length(network)*(length(network)-1)); 
	
	for i=1:1:size(network)(1);
		V = find(network(i,:));
		S = network(V, V);
		k = size(S)(1) * (size(S)(1)-1);
			
		if k == 0;
			sigma(i) = 0;
		else;
			sigma(i) = (sum(S(:))) / k;			
		end;
	end;			
	
	C = sum(sigma) / size(sigma)(2);
	
end;




