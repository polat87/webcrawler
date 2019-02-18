%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%						  Degree Distribution						   %
%						GOEKHAN POLAT (0830690)						   %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% TODO: implement a function that calculates the degree distribution and
%       plot the results in a file "networkDegreesB.png" using Octave plotting functionality
% INPUT: adjacency matrix (nxn) of the one-mode network
% OUTPUT: degree vector (1xn, integers)
function [degree_vec] = degreeDistribution(network) 
    degree_vec = zeros(1, size(network, 1));
    
    for m=1:1:size(network);
		degree_vec(sum(network(m,:)))+= 1;
	end;
	
	x_max_index = 0;
	values = [];	
	for i=1:size(degree_vec)(2);  
		if (degree_vec(i) > 0);
			x_max_index = i;
			values(i) = degree_vec(i);
		end;
	end;
	
	bar(values);
	title("Degree Distribution");
	xlabel("Number of Edges");
	ylabel("Number of Nodes");
	print("networkDegreesB.png");

end;

