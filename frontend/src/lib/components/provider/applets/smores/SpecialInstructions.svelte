<script lang="ts">
    let { quotedata } = $props();
</script>

<div
    class="flex flex-col gap-3 w-full bg-stone-100 border-stone-300 border-2 p-3 text-stone-700 rounded-2xl"
>
    <div class="font-bold text-xl">
        <span>Special Instructions</span>
    </div>

        <div class="w-full grid place-items-center">
            <div class="w-9/10 bg-emerald-300 p-3 items-cente rounded-lg">
                <div class="w-1/2 text-stone-800">
                    {quotedata.specialInstructions} 
                </div>
            </div>
        </div>

</div>
