#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet


class BookView(ViewSet):
    def list(self, request: Request) -> Response:
        return Response({"data": "List of books"}, status.HTTP_200_OK)

    def create(self, request: Request) -> Response:
        # title: str = request.data.get("title")
        # author: str = request.data.get("author")
        return Response({"message": "Book created"}, status.HTTP_201_CREATED)

    def update(self, request: Request, pk: int = 0) -> Response:
        if pk == 1:
            return Response({"message": "successfully updated"}, status.HTTP_200_OK)
        else:
            return Response({"message": "not found"}, status.HTTP_404_NOT_FOUND)

    def retrieve(self, request: Request, pk: int) -> Response:
        return Response({"message": f"book with id: {str(pk)}"}, status.HTTP_200_OK)

    def destroy(self, request: Request, pk: int | None = None) -> Response:
        if pk == 1:
            return Response(
                {"message": f"Book no. {pk} is deleted"}, status.HTTP_200_OK
            )
        return Response(
            {"message": f"Book no. {pk} not found"}, status.HTTP_404_NOT_FOUND
        )
