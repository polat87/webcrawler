%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%						  Get Number of Edges						   %
%						GOEKHAN POLAT (0830690)						   %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% TODO: implement a function that calculates the number of edges
% INPUT: adjacency matrix (nxn) of the one-mode network
% OUTPUT: number of edges (integer)
function [num_edges] = getNumEdges(network)
    num_edges = 0;
        
    for m=1:1:size(network)(1);
        for n=m:1:size(network)(2);
			if network(m,n) == 1;
			num_edges+=1;
			end;
		end;
	end;
	
end;
