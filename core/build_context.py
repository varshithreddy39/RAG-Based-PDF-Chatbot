def build_context(chunks):
    context_parts = []
    for i, chunk in enumerate(chunks, start=1):
        context_parts.append(f"[Context {i}]\n{chunk}")
    return "\n\n".join(context_parts)
