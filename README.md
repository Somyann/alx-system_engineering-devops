listings
Many endpoints on reddit use the same protocol for controlling pagination and filtering. These endpoints are called Listings and share five common parameters: after / before, limit, count, and show.

Listings do not use page numbers because their content changes so frequently. Instead, they allow you to view slices of the underlying data. Listing JSON responses contain after and before fields which are equivalent to the "next" and "prev" buttons on the site and in combination with count can be used to page through the listing.
